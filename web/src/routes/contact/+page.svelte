<script lang="ts">
  import { t } from '$lib/i18n';
  let emailVisible = false;
  const revealEmail = () => {
    emailVisible = true;
    navigator.clipboard.writeText('contact@robertovallado.dev');
  };
</script>

<svelte:head>
  <title>{$t('contact.page_title')}</title>
</svelte:head>

<h1>{$t('contact.h1')}</h1>

<p>{$t('contact.intro')}</p>
<p>
  {$t('contact.email_label')}
  {#if emailVisible}
    <a href="mailto:contact@robertovallado.dev">contact@robertovallado.dev</a>
  {:else}
    <button on:click={revealEmail} class="small-btn no-float" title={$t('contact.reveal')}>
      {$t('contact.reveal')}
    </button>
  {/if}
</p>
<p>{$t('contact.thanks')}</p>

<div class="some-text">
  <p>
    {$t('contact.learn_more')} <a href="/intro">{$t('contact.intro_page')}</a>
    {$t('contact.browse')}
    <a href="/skills">{$t('contact.skills_page')}</a>,
    <a href="/experience">{$t('contact.experience_page')}</a> {$t('achievements.and') || 'and'}
    <a href="/achievements">{$t('contact.achievements_page')}</a>
    {$t('contact.fit')}
  </p>
  <p>
    {$t('contact.pdf')} <a href="/download">{$t('contact.here')}</a>.
  </p>
  <p>
    {$t('contact.also_on')}
    <a href="https://www.linkedin.com/in/roberto-vallado/" target="_blank">LinkedIn</a>
    {$t('contact.and')}
    <a href="https://github.com/RobertoVallado" target="_blank">GitHub</a>.
  </p>
  <p>
    {$t('contact.ideal_role')} <a href="/ideal-role">{$t('contact.ideal_role_page')}</a>{$t('contact.ideal_role_end')}
  </p>
  <p>{$t('contact.references')}</p>
</div>

<style lang="scss">
.some-text {
  font-size: 0.8rem;
  border: 2px solid var(--primary);
  padding: 0.25rem 0.5rem;
  margin: 2rem auto 1rem auto;
  border-radius: 4px;
  background: var(--primary-transparent);
  b, a { font-weight: 500; }
}
</style>
